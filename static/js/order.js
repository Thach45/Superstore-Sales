formSearch = document.querySelector('.form-Search');
let sortTotalcost = document.querySelector('.btn-sortCost');
let sortFre = document.querySelector('.btn-sortFre');// Giả sử phần tử sort có class là 'sort-element'
let sortAscending = true; // Biến để theo dõi trạng thái hiện tại
const filterShip = document.querySelector('.orderFilter');
const filterOrder = document.querySelector('.shipFilter');
const applyFilter = document.querySelector('#applyFilters');

if (formSearch) {
    formSearch.addEventListener('submit', function (e) {
        e.preventDefault();
        let search = document.querySelector('.search').value;
        
        if (search) {
            if (search[2] =="-") {
                window.location.href = '/order/search?IDCustomer=' + encodeURIComponent(search);
            }
            else
                window.location.href = '/order/search?Name=' + encodeURIComponent(search);
        } else {
            window.location.href = '/';
        }
    });
}
//chức năng sort
if (sortTotalcost) {
    sortTotalcost.addEventListener('click', function () {
        if (sortTotalcost) {
            if (sortAscending) {
                sortTotalcost.name = 'asc'; // Thay đổi giá trị của thuộc tính name thành tăng dần
                sortAscending = false; // Chuyển trạng thái sang giảm dần
            } else {
                sortTotalcost.name = 'desc'; // Thay đổi giá trị của thuộc tính name thành giảm dần
                sortAscending = true; // Chuyển trạng thái sang tăng dần
            }
            window.location.href = '/order/sort?key=Totalcost&sort=' + sortTotalcost.name; // Chuyển hướng trang với tham số sort
        }
    });
}
if (sortFre) {
    sortFre.addEventListener('click', function () {
        if (sortFre) {
            if (sortAscending) {
                sortFre.name = 'asc'; // Thay đổi giá trị của thuộc tính name thành tăng dần
                sortAscending = false; // Chuyển trạng thái sang giảm dần
            } else {
                sortFre.name = 'desc'; // Thay đổi giá trị của thuộc tính name thành giảm dần
                sortAscending = true; // Chuyển trạng thái sang tăng dần
            }
            console.log(sortFre.name);
            window.location.href = '/order/sort?key=Fre&sort=' + sortFre.name; // Chuyển hướng trang với tham số sort
        }
    });
}
//chức năng filter
if (applyFilter) {
    applyFilter.addEventListener('click', function () {
        let ship = filterShip.value;
        let order = filterOrder.value;
        window.location.href = '/order/filter?Shipper=' + ship + '&Order=' + order;
       
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
            if (currentPage < totalPages) {
                urlParams.set('page', currentPage + 1);
                window.location.search = urlParams.toString();
            }
        });
    }
});