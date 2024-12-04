formSearch = document.querySelector('.form-Search');

let sortElement = document.querySelector('.btn-sort'); // Giả sử phần tử sort có class là 'sort-element'
let sortAscending = true; // Biến để theo dõi trạng thái hiện tại
const filterCity = document.querySelector('.cityFilter');
const filterSegment = document.querySelector('.segmentFilter');
const filterRegion = document.querySelector('.regionFilter');
const filterState = document.querySelector('.stateFilter');

const applyFilter = document.querySelector('#applyFilters');
//chức năng tìm kiếm
if (formSearch) {
    formSearch.addEventListener('submit', function (e) {
        e.preventDefault();
        let search = document.querySelector('.search').value;
        
        if (search) {
            if (search[2] =="-") {
                window.location.href = '/customer/search?IDCustomer=' + encodeURIComponent(search);
            }
            else
                window.location.href = '/customer/search?Name=' + encodeURIComponent(search);
        } else {
            window.location.href = '/';
        }
    });
}
//chức năng sort
if (sortElement) {
    sortElement.addEventListener('click', function () {
        if (sortElement) {
            if (sortAscending) {
                sortElement.name = 'asc'; // Thay đổi giá trị của thuộc tính name thành tăng dần
                sortAscending = false; // Chuyển trạng thái sang giảm dần
            } else {
                sortElement.name = 'desc'; // Thay đổi giá trị của thuộc tính name thành giảm dần
                sortAscending = true; // Chuyển trạng thái sang tăng dần
            }
            console.log(sortElement.name);
            window.location.href = '/customer/sort?sort=' + sortElement.name; // Chuyển hướng trang với tham số sort
        }
    });
}
//chức năng filter
if (applyFilter) {
    applyFilter.addEventListener('click', function () {
        let city = filterCity.value;
        let region = filterRegion.value;
        let state = filterState.value;
        let segment = filterSegment.value;
        window.location.href = '/customer/filter?City=' + city + '&Segment=' + segment + '&Region=' + region + '&State=' + state;
       
    });
}

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
            if (currentPage) {
                urlParams.set('page', currentPage + 1);
                window.location.search = urlParams.toString();
            }
        });
    }
});

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
            window.location.href = '/product/sort?field=Quantity&sort=' + sortQuantityProduct.name;  // Chuyển hướng trang với tham số sort
        }
    });
}

const addCustomer = document.querySelector('.btn-add');
const addCustomerForm = document.querySelector('.add-customer-form');
if (addCustomer) {
    addCustomer.addEventListener('click', function () {
        addCustomerForm.classList.remove('d-none');
    });
}

const closeForm = document.querySelector('.btn-close');
if (closeForm) {
    closeForm.addEventListener('click', function () {
        addCustomerForm.classList.add('d-none');
    });
}