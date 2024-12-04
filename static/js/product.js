document.addEventListener('DOMContentLoaded', function () {
    let paginationLinks = document.querySelectorAll('.pagination .page-link');
    let urlParams = new URLSearchParams(window.location.search);
    
    paginationLinks.forEach(function (link) {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            let page = this.getAttribute('data-page');
            if (page) {
                urlParams.set('page', page);
                window.location.search = urlParams.toString();
            }
        });
    });

    let prevPage = document.getElementById('prevPage');
    let nextPage = document.getElementById('nextPage');
    console.log(nextPage);
    let currentPage = parseInt(urlParams.get('page')) || 1;

    if (prevPage) {
        prevPage.addEventListener('click', function (e) {
            e.preventDefault();
            if (currentPage > 1) {
                urlParams.set('page', currentPage - 1);
                window.location.search = urlParams.toString();
            }
        });
    }

    if (nextPage) {
        nextPage.addEventListener('click', function (e) {
            e.preventDefault();
            if (currentPage) {
                urlParams.set('page', currentPage + 1);
                window.location.search = urlParams.toString();
            }
        });
    }
});

sortAscending = true; // Biến lưu trạng thái sắp xếp tăng dần hay giảm dần  

//chức năng tìm kiếm
// Kiểm tra nếu phần tử formSearch tồn tại
const formSearch = document.querySelector('.form-Search');

if (formSearch) {
    // Thêm sự kiện khi người dùng submit form
    formSearch.addEventListener('submit', function (e) {
        e.preventDefault(); // Ngừng hành động mặc định của form (không reload trang)

        // Lấy giá trị tìm kiếm từ trường input trong form
        let search = formSearch.querySelector('.search').value.trim(); // Tìm input bên trong form

        // Nếu có giá trị tìm kiếm, chuyển hướng đến trang tìm kiếm sản phẩm
        if (search) {
            window.location.href = '/product/search?ProductName=' + encodeURIComponent(search);
        } else {
            // Nếu không có giá trị tìm kiếm, chuyển hướng về trang chủ
            window.location.href = '/';
        }
    });
}



sortAscending = true; // Biến lưu trạng thái sắp xếp tăng dần hay giảm dần  


//chức năng sort
const sortSaleProduct = document.querySelector(".btn-sort-saleProduct")
if (sortSaleProduct) {
    sortSaleProduct.addEventListener('click', function () {
        if (sortSaleProduct) {
            if (sortAscending) {
                sortSaleProduct.name = 'asc'; // Thay đổi giá trị của thuộc tính name thành tăng dần
                sortAscending = false; // Chuyển trạng thái sang giảm dần
            } else {
                sortSaleProduct.name = 'desc'; // Thay đổi giá trị của thuộc tính name thành giảm dần
                sortAscending = true; // Chuyển trạng thái sang tăng dần
            }
            console.log(sortSaleProduct.name);
            window.location.href = '/product/sort?field=Revenue&sort=' + sortSaleProduct.name;
            // window.location.href = '/product/sort?sort=' + sortElementProduct.name; // Chuyển hướng trang với tham số sort
        }
    });
}

//chức năng sort
const sortQuantityProduct = document.querySelector(".btn-sort-quantityProduct")
if (sortQuantityProduct) {
    sortQuantityProduct.addEventListener('click', function () {
        if (sortQuantityProduct) {
            if (sortAscending) {
                sortQuantityProduct.name = 'asc'; // Thay đổi giá trị của thuộc tính name thành tăng dần
                sortAscending = false; // Chuyển trạng thái sang giảm dần
            } else {
                sortQuantityProduct.name = 'desc'; // Thay đổi giá trị của thuộc tính name thành giảm dần
                sortAscending = true; // Chuyển trạng thái sang tăng dần
            }
            window.location.href = '/product/sort?field=Quantity&sort=' + sortQuantityProduct.name;
            // window.location.href = '/product/sort?sort=' + sortQuantityProduct.name; // Chuyển hướng trang với tham số sort
        }
    });
}

//filter product

const categoryData = {
    Furniture: ['Bookcases', 'Chairs', 'Furnishings', 'Tables'],
    OfficeSupplies: ['Appliances', 'Envelopes', 'Fasteners', 'Labels', 'Art', 'Binders', 'Paper', 'Supplies', 'Storage'],
    Technology: ['Machines', 'Accessories', 'Copiers', 'Phones']
}

// Thêm event listener cho category select
const categorySelect = document.getElementById('category');
if (categorySelect) {
    categorySelect.addEventListener('change', function() {
        const selectedCategory = this.value;
        console.log(selectedCategory);
        const subcategoryGroups = document.querySelectorAll(".subcategory-group");
        
        // Ẩn tất cả các subcategory groups
        subcategoryGroups.forEach(group => {
            group.style.display = "none";
        });

        // Nếu category được chọn không phải "All Category"
        if (selectedCategory !== "All Category") {
            const selectedGroup = document.getElementById(selectedCategory);
            if (selectedGroup) {
                selectedGroup.style.display = "block";
            }
            updateSubcategoryOptions(selectedCategory);
        }
    });
}

function updateSubcategoryOptions(category) {
    const subcategorySelect = document.querySelector(`#subcategory-${category.toLowerCase()}`);
    if (!subcategorySelect) return;
    
    const subCategories = categoryData[category] || [];
    subcategorySelect.innerHTML = '';

    // Thêm option mặc định "All Sub-Category"
    const allOption = document.createElement('option');
    allOption.value = 'All Sub-Category';
    allOption.textContent = 'All Sub-Category';
    subcategorySelect.appendChild(allOption);

    // Thêm các sub-categories
    subCategories.forEach(subCategory => {
        const option = document.createElement('option');
        option.value = subCategory;
        option.textContent = subCategory;
        subcategorySelect.appendChild(option);
    });
}

const filterCategory = document.querySelector('.categoryFilter');
const applyFilter = document.getElementById('applyFilter');

if (applyFilter) {
    applyFilter.addEventListener('click', function () {
        const category = filterCategory.value;
        // Chuyển "All Category" thành chuỗi rỗng để filter
        const newcategory = category === "All Category" ? "" : category;
        
        // Lấy subcategory đang được hiển thị và được chọn
        let selectedSubCategories = [];
        if (category !== "All Category") {
            const activeSubSelect = document.querySelector(`#subcategory-${category.toLowerCase()}`);
            if (activeSubSelect) {
                selectedSubCategories = Array.from(activeSubSelect.selectedOptions).map(option => option.value);
            }
        }

        // Xử lý trường hợp "All Sub-Category" hoặc không có subcategory nào được chọn
        if (selectedSubCategories.length === 0 || selectedSubCategories.includes("All Sub-Category")) {
            selectedSubCategories = [''];
        }

        const sub = selectedSubCategories.join(',');

        // Chuyển hướng với params
        window.location.href = '/product/filter?Category=' + newcategory + '&Sub-Category=' + sub;
    });
}

const addProduct = document.querySelector('.add-product');
const addProductForm = document.querySelector('.add-product-form');
if (addProduct) {
    addProduct.addEventListener('click', function () {
        addProductForm.classList.remove('d-none');
    });
}

const subcategoryEdit = document.getElementById('SubCategory');
const categoryEdit = document.getElementById('Category');
if (categoryEdit && subcategoryEdit) {
    categoryEdit.addEventListener('change', function () {
        subcategoryEdit.innerHTML = '';
        updateSubcategoryOptions(categoryEdit,subcategoryEdit);
    });
}
const addCategory = document.getElementById('addCategory');
const addSubCategory = document.getElementById('addSubCategory');
if (addCategory && addSubCategory) {
    addCategory.addEventListener('change', function () {
        addSubCategory.innerHTML = '';
        updateSubcategoryOptions(addCategory,addSubCategory);
    });
}

function updateSubcategoryOptions(Category,subCategory) {
    if (Category) {
        if (Category.value === "Furniture") {
        for (let i = 0; i < categoryData.Furniture.length; i++) {
            subCategory.innerHTML += `<option value="${categoryData.Furniture[i]}">${categoryData.Furniture[i]}</option>`;
        }
    }
    if (Category.value === "OfficeSupplies") {
        for (let i = 0; i < categoryData.OfficeSupplies.length; i++) {
            subCategory.innerHTML += `<option value="${categoryData.OfficeSupplies[i]}">${categoryData.OfficeSupplies[i]}</option>`;
        }
    }
    if (Category.value === "Technology") {
        for (let i = 0; i < categoryData.Technology.length; i++) {
            subCategory.innerHTML += `<option value="${categoryData.Technology[i]}">${categoryData.Technology[i]}</option>`;
            }
        }
    }
}

const closeForm = document.querySelector('.btn-close');
if (closeForm) {
    closeForm.addEventListener('click', function () {
        addProductForm.classList.add('d-none');
    });
}