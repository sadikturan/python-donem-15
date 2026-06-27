const API_BASE = (() => {
  const configured = window.NORTHWIND_API?.replace(/\/$/, "");
  if (configured) return configured;

  const { protocol, port, origin } = window.location;
  if ((protocol === "http:" || protocol === "https:") && port === "8000") {
    return origin;
  }

  return "http://127.0.0.1:8000";
})();

const state = {
  tab: "customers",
  data: { customers: [], categories: [], products: [] },
  editing: null,
};

const tabConfig = {
  customers: {
    title: "Müşteriler",
    endpoint: "/customers",
    idField: "CustomerID",
    columns: [
      { key: "CustomerID", label: "ID" },
      { key: "CompanyName", label: "Şirket" },
      { key: "ContactName", label: "Yetkili" },
      { key: "City", label: "Şehir" },
      { key: "Country", label: "Ülke" },
    ],
    fields: [
      { name: "CustomerID", label: "Müşteri ID", type: "text", required: true, maxLength: 5, createOnly: true },
      { name: "CompanyName", label: "Şirket Adı", type: "text", required: true, maxLength: 40 },
      { name: "ContactName", label: "Yetkili", type: "text", maxLength: 30 },
      { name: "ContactTitle", label: "Unvan", type: "text", maxLength: 30 },
      { name: "Address", label: "Adres", type: "text", maxLength: 60 },
      { name: "City", label: "Şehir", type: "text", maxLength: 15 },
      { name: "Region", label: "Bölge", type: "text", maxLength: 15 },
      { name: "PostalCode", label: "Posta Kodu", type: "text", maxLength: 10 },
      { name: "Country", label: "Ülke", type: "text", maxLength: 15 },
      { name: "Phone", label: "Telefon", type: "text", maxLength: 24 },
      { name: "Fax", label: "Faks", type: "text", maxLength: 24 },
    ],
  },
  categories: {
    title: "Kategoriler",
    endpoint: "/categories",
    idField: "CategoryID",
    columns: [
      { key: "CategoryID", label: "ID" },
      { key: "CategoryName", label: "Kategori" },
      { key: "Description", label: "Açıklama" },
    ],
    fields: [
      { name: "CategoryName", label: "Kategori Adı", type: "text", required: true, maxLength: 15 },
      { name: "Description", label: "Açıklama", type: "textarea" },
    ],
  },
  products: {
    title: "Ürünler",
    endpoint: "/products",
    idField: "ProductID",
    columns: [
      { key: "ProductID", label: "ID" },
      { key: "ProductName", label: "Ürün" },
      { key: "CategoryName", label: "Kategori" },
      { key: "UnitPrice", label: "Fiyat" },
      { key: "UnitsInStock", label: "Stok" },
      { key: "Discontinued", label: "Durum" },
    ],
    fields: [
      { name: "ProductName", label: "Ürün Adı", type: "text", required: true, maxLength: 40 },
      { name: "CategoryID", label: "Kategori", type: "select", optionsFrom: "categories", optionValue: "CategoryID", optionLabel: "CategoryName" },
      { name: "SupplierID", label: "Tedarikçi ID", type: "number" },
      { name: "QuantityPerUnit", label: "Birim", type: "text", maxLength: 20 },
      { name: "UnitPrice", label: "Birim Fiyat", type: "number", step: "0.01" },
      { name: "UnitsInStock", label: "Stok", type: "number" },
      { name: "UnitsOnOrder", label: "Siparişte", type: "number" },
      { name: "ReorderLevel", label: "Yeniden Sipariş", type: "number" },
      { name: "Discontinued", label: "Üretimi durduruldu", type: "checkbox" },
    ],
  },
};

const els = {
  tabs: document.getElementById("tabs"),
  tableHead: document.getElementById("table-head"),
  tableBody: document.getElementById("table-body"),
  pageTitle: document.getElementById("page-title"),
  recordCount: document.getElementById("record-count"),
  loading: document.getElementById("loading"),
  toast: document.getElementById("toast"),
  modal: document.getElementById("modal"),
  modalTitle: document.getElementById("modal-title"),
  modalForm: document.getElementById("modal-form"),
  btnNew: document.getElementById("btn-new"),
  btnRefresh: document.getElementById("btn-refresh"),
  btnCloseModal: document.getElementById("btn-close-modal"),
  btnCancel: document.getElementById("btn-cancel"),
  apiStatus: document.getElementById("api-status"),
  apiHint: document.getElementById("api-hint"),
};

async function apiRequest(path, options = {}) {
  let response;
  try {
    response = await fetch(`${API_BASE}${path}`, {
      headers: { "Content-Type": "application/json", ...(options.headers || {}) },
      ...options,
    });
  } catch {
    throw new Error(`API'ye ulaşılamıyor: ${API_BASE}${path}`);
  }

  if (response.status === 204) return null;

  let payload = null;
  const text = await response.text();
  if (text) {
    try {
      payload = JSON.parse(text);
    } catch {
      payload = text;
    }
  }

  if (!response.ok) {
    const detail = payload?.detail;
    const message = Array.isArray(detail)
      ? detail.map((item) => item.msg).join(", ")
      : detail || `HTTP ${response.status}`;
    throw new Error(message);
  }

  return payload;
}

function showToast(message, type = "success") {
  els.toast.textContent = message;
  els.toast.className = `fixed bottom-6 right-6 z-50 rounded-xl px-4 py-3 text-sm font-medium shadow-lg transition ${
    type === "success" ? "bg-emerald-600 text-white" : "bg-rose-600 text-white"
  }`;
  els.toast.classList.remove("hidden");
  setTimeout(() => els.toast.classList.add("hidden"), 3200);
}

function setLoading(isLoading) {
  els.loading.classList.toggle("hidden", !isLoading);
}

function formatCell(key, row) {
  if (key === "Discontinued") {
    return row[key]
      ? '<span class="rounded-full bg-rose-100 px-2 py-1 text-xs font-medium text-rose-700">Durduruldu</span>'
      : '<span class="rounded-full bg-emerald-100 px-2 py-1 text-xs font-medium text-emerald-700">Aktif</span>';
  }
  if (key === "UnitPrice" && row[key] != null) {
    return `$${Number(row[key]).toFixed(2)}`;
  }
  return row[key] ?? "—";
}

function enrichProducts(products, categories) {
  const categoryMap = Object.fromEntries(categories.map((c) => [c.CategoryID, c.CategoryName]));
  return products.map((product) => ({
    ...product,
    CategoryName: categoryMap[product.CategoryID] || "—",
  }));
}

async function loadAll() {
  setLoading(true);
  els.apiHint.classList.add("hidden");
  els.apiStatus.textContent = "Bağlanıyor...";
  els.apiStatus.className = "rounded-full bg-slate-100 px-3 py-1 text-xs font-medium text-slate-600";

  try {
    const [customers, categories, products] = await Promise.all([
      apiRequest("/customers"),
      apiRequest("/categories"),
      apiRequest("/products"),
    ]);
    state.data.customers = customers;
    state.data.categories = categories;
    state.data.products = enrichProducts(products, categories);
    els.apiStatus.textContent = "API bağlı";
    els.apiStatus.className = "rounded-full bg-emerald-100 px-3 py-1 text-xs font-medium text-emerald-700";
    renderTable();
  } catch (error) {
    els.apiStatus.textContent = "API bağlantısı yok";
    els.apiStatus.className = "rounded-full bg-rose-100 px-3 py-1 text-xs font-medium text-rose-700";
    els.apiHint.textContent = `${error.message}. Sayfayı http://127.0.0.1:8000 adresinden açın ve uvicorn'un çalıştığından emin olun.`;
    els.apiHint.classList.remove("hidden");
    showToast(error.message, "error");
  } finally {
    setLoading(false);
  }
}

function renderTabs() {
  els.tabs.innerHTML = Object.entries(tabConfig)
    .map(
      ([key, config]) => `
      <button
        data-tab="${key}"
        class="tab-btn rounded-xl px-4 py-2 text-sm font-medium transition ${
          state.tab === key
            ? "bg-slate-900 text-white shadow"
            : "bg-white text-slate-600 hover:bg-slate-100"
        }"
      >
        ${config.title}
      </button>`
    )
    .join("");

  els.tabs.querySelectorAll(".tab-btn").forEach((button) => {
    button.addEventListener("click", () => {
      state.tab = button.dataset.tab;
      renderTabs();
      renderTable();
    });
  });
}

function renderTable() {
  const config = tabConfig[state.tab];
  const rows = state.data[state.tab];

  els.pageTitle.textContent = config.title;
  els.recordCount.textContent = `${rows.length} kayıt`;

  els.tableHead.innerHTML = `
    <tr>
      ${config.columns.map((col) => `<th class="px-4 py-3 text-left text-xs font-semibold uppercase tracking-wide text-slate-500">${col.label}</th>`).join("")}
      <th class="px-4 py-3 text-right text-xs font-semibold uppercase tracking-wide text-slate-500">İşlemler</th>
    </tr>`;

  if (!rows.length) {
    els.tableBody.innerHTML = `
      <tr>
        <td colspan="${config.columns.length + 1}" class="px-4 py-10 text-center text-slate-500">
          Kayıt bulunamadı.
        </td>
      </tr>`;
    return;
  }

  els.tableBody.innerHTML = rows
    .map((row) => {
      const id = row[config.idField];
      return `
        <tr class="border-t border-slate-100 hover:bg-slate-50">
          ${config.columns.map((col) => `<td class="px-4 py-3 text-sm text-slate-700">${formatCell(col.key, row)}</td>`).join("")}
          <td class="px-4 py-3 text-right">
            <button data-action="edit" data-id="${id}" class="mr-2 rounded-lg bg-slate-100 px-3 py-1.5 text-xs font-medium text-slate-700 hover:bg-slate-200">Düzenle</button>
            <button data-action="delete" data-id="${id}" class="rounded-lg bg-rose-50 px-3 py-1.5 text-xs font-medium text-rose-700 hover:bg-rose-100">Sil</button>
          </td>
        </tr>`;
    })
    .join("");

  els.tableBody.querySelectorAll("button").forEach((button) => {
    button.addEventListener("click", () => {
      const id = button.dataset.id;
      if (button.dataset.action === "edit") openModal("edit", id);
      if (button.dataset.action === "delete") deleteRecord(id);
    });
  });
}

function buildFieldHtml(field, value, isEdit) {
  if (field.createOnly && isEdit) return "";

  const common = `name="${field.name}" id="field-${field.name}" ${
    field.required ? "required" : ""
  } ${field.maxLength ? `maxlength="${field.maxLength}"` : ""}`;

  if (field.type === "textarea") {
    return `
      <label class="block">
        <span class="mb-1 block text-sm font-medium text-slate-700">${field.label}</span>
        <textarea ${common} rows="3" class="w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-slate-400">${value ?? ""}</textarea>
      </label>`;
  }

  if (field.type === "select") {
    const options = state.data[field.optionsFrom] || [];
    return `
      <label class="block">
        <span class="mb-1 block text-sm font-medium text-slate-700">${field.label}</span>
        <select ${common} class="w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-slate-400">
          <option value="">Seçiniz</option>
          ${options
            .map(
              (item) =>
                `<option value="${item[field.optionValue]}" ${
                  String(item[field.optionValue]) === String(value ?? "") ? "selected" : ""
                }>${item[field.optionLabel]}</option>`
            )
            .join("")}
        </select>
      </label>`;
  }

  if (field.type === "checkbox") {
    return `
      <label class="flex items-center gap-2 rounded-xl border border-slate-200 px-3 py-2">
        <input type="checkbox" ${common} class="h-4 w-4" ${value ? "checked" : ""} />
        <span class="text-sm font-medium text-slate-700">${field.label}</span>
      </label>`;
  }

  return `
    <label class="block">
      <span class="mb-1 block text-sm font-medium text-slate-700">${field.label}</span>
      <input
        type="${field.type}"
        ${common}
        ${field.step ? `step="${field.step}"` : ""}
        value="${value ?? ""}"
        class="w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-slate-400"
      />
    </label>`;
}

function openModal(mode, id = null) {
  const config = tabConfig[state.tab];
  const isEdit = mode === "edit";
  const record = isEdit ? state.data[state.tab].find((item) => String(item[config.idField]) === String(id)) : null;

  state.editing = isEdit ? record : null;
  els.modalTitle.textContent = isEdit ? `${config.title} Düzenle` : `Yeni ${config.title.slice(0, -1) || config.title}`;
  els.modalForm.innerHTML = config.fields
    .map((field) => buildFieldHtml(field, record?.[field.name], isEdit))
    .join("");
  els.modal.classList.remove("hidden");
}

function closeModal() {
  state.editing = null;
  els.modal.classList.add("hidden");
  els.modalForm.innerHTML = "";
}

function readFormData() {
  const config = tabConfig[state.tab];
  const formData = new FormData(els.modalForm);
  const payload = {};

  for (const field of config.fields) {
    if (field.createOnly && state.editing) continue;

    if (field.type === "checkbox") {
      payload[field.name] = formData.has(field.name);
      continue;
    }

    const value = formData.get(field.name);
    if (value === "" || value === null) {
      if (!state.editing) payload[field.name] = null;
      continue;
    }

    if (field.type === "number") {
      payload[field.name] = Number(value);
    } else {
      payload[field.name] = value;
    }
  }

  return payload;
}

async function saveRecord(event) {
  event.preventDefault();
  const config = tabConfig[state.tab];
  const payload = readFormData();

  try {
    if (state.editing) {
      const id = state.editing[config.idField];
      await apiRequest(`${config.endpoint}/${encodeURIComponent(id)}`, {
        method: "PUT",
        body: JSON.stringify(payload),
      });
      showToast("Kayıt güncellendi.");
    } else {
      await apiRequest(config.endpoint, {
        method: "POST",
        body: JSON.stringify(payload),
      });
      showToast("Kayıt eklendi.");
    }
    closeModal();
    await loadAll();
  } catch (error) {
    showToast(error.message, "error");
  }
}

async function deleteRecord(id) {
  const config = tabConfig[state.tab];
  if (!confirm("Bu kaydı silmek istediğinize emin misiniz?")) return;

  try {
    await apiRequest(`${config.endpoint}/${encodeURIComponent(id)}`, { method: "DELETE" });
    showToast("Kayıt silindi.");
    await loadAll();
  } catch (error) {
    showToast(error.message, "error");
  }
}

els.btnNew.addEventListener("click", () => openModal("create"));
els.btnRefresh.addEventListener("click", loadAll);
els.btnCloseModal.addEventListener("click", closeModal);
els.btnCancel.addEventListener("click", closeModal);
els.modalForm.addEventListener("submit", saveRecord);
els.modal.addEventListener("click", (event) => {
  if (event.target === els.modal) closeModal();
});

renderTabs();
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", loadAll);
} else {
  loadAll();
}
