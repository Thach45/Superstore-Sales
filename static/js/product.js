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

function update() {
    const categorySelect = document.getElementById('category');
    const selectedCategory = categorySelect.value;

    var subcategoryGroups = document.querySelectorAll(".subcategory-group");
    
    subcategoryGroups.forEach(function(group) {
        if (group.id === selectedCategory) {
            group.style.display = "block";
            document.getElementById("category").classList.add("shrink");
        } else {
            group.style.display = "none";
            document.getElementById("category").classList.remove("shrink");
            return;
        }
    });
    
    updateSubcategoryOptions(selectedCategory);
}

function updateSubcategoryOptions(category) {
    const subcategorySelect = document.querySelector(`#subcategory-${category.toLowerCase()}`);
    const subCategories = categoryData[category] || [];
    
    subcategorySelect.innerHTML = '';

    const allOption = document.createElement('option');
    allOption.value = 'All Sub-Category';
    allOption.textContent = 'All Sub-Category';
    subcategorySelect.appendChild(allOption);

    subCategories.forEach(subCategory => {
        const option = document.createElement('option');
        option.value = subCategory;
        option.textContent = subCategory;
        subcategorySelect.appendChild(option);
    });
}
window.onload = update;

const filterCategory = document.querySelector('.categoryFilter');
const filterSub = document.querySelector('.subFilter');
console.log(filterSub);
if (applyFilter) {
    applyFilter.addEventListener('click', function () {
        const category = filterCategory.value;
        console.log(category);
        console.log(sub);
        const newcategory= category === "All Category" ? "" : category;

        const selectedSubCategories = Array.from(filterSub.selectedOptions).map(option => console.log(option.value));
        console.log(selectedSubCategories);
        if (selectedSubCategories.length === 0 || selectedSubCategories.includes("All Sub-Category")) {
            selectedSubCategories.length = 0;
            selectedSubCategories.push('');  
        }
        const sub = selectedSubCategories.join(',');
        

        window.location.href = '/product/filter?Category=' + newcategory + '&Sub-Category=' + sub;
    });
}