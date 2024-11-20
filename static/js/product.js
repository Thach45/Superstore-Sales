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
            if (currentPage < totalPages) {
                urlParams.set('page', currentPage + 1);
                window.location.search = urlParams.toString();
            }
        });
    }
});

sortAscending = true; // Biến lưu trạng thái sắp xếp tăng dần hay giảm dần  

//chức năng sort
// const sortSaleProduct = document.querySelector(".btn-sort-saleProduct")
// if (sortSaleProduct) {
//     sortSaleProduct.addEventListener('click', function () {
//         if (sortSaleProduct) {
//             if (sortAscending) {
//                 sortSaleProduct.name = 'asc'; // Thay đổi giá trị của thuộc tính name thành tăng dần
//                 sortAscending = false; // Chuyển trạng thái sang giảm dần
//             } else {
//                 sortSaleProduct.name = 'desc'; // Thay đổi giá trị của thuộc tính name thành giảm dần
//                 sortAscending = true; // Chuyển trạng thái sang tăng dần
//             }
//             console.log(sortSaleProduct.name);
//             window.location.href = '/product/sort?field=Sales&sort=' + sortSaleProduct.name;
//             // window.location.href = '/product/sort?sort=' + sortElementProduct.name; // Chuyển hướng trang với tham số sort
//         }
//     });
// }

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
            window.location.href = '/product/sort?field=Sales&sort=' + sortSaleProduct.name;
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