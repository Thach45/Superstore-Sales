
let sortTotalcost = document.querySelector('.btn-sortCost');
let sortFre = document.querySelector('.btn-sortFre');// Giả sử phần tử sort có class là 'sort-element'
let sortAscending = true; // Biến để theo dõi trạng thái hiện tại
const filterShip = document.querySelector('.orderFilter');
const filterOrder = document.querySelector('.shipFilter');
const applyFilter = document.querySelector('#applyFilters');

//chức năng tìm kiếm
const formSearch = document.querySelector('.form-Search');

if (formSearch) {
    // Thêm sự kiện khi người dùng submit form
    formSearch.addEventListener('submit', function (e) {
        e.preventDefault(); // Ngừng hành động mặc định của form (không reload trang)

        // Lấy giá trị tìm kiếm từ trường input trong form
        let search = formSearch.querySelector('.search').value.trim(); // Tìm input bên trong form và loại bỏ khoảng trắng

        // Nếu có giá trị tìm kiếm, chuyển hướng đến trang tìm kiếm đơn hàng
        if (search) {
            // Chuyển hướng đến trang kết quả tìm kiếm với tham số OrderID
            window.location.href = '/order/search?OrderID=' + encodeURIComponent(search);
        } else {
            // Nếu không có giá trị tìm kiếm, chuyển hướng về trang chủ
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
            window.location.href = "/order/sort?field=TotalCost&sort="+sortTotalcost.name;
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
            window.location.href = "/order/sort?field=Frequency&sort="+sortFre.name;
        }
    });
}




//chức năng filter

if (applyFilter) {
    applyFilter.addEventListener('click', function () {
        let ship = document.querySelector('.shipFilter').value;
        let order = document.querySelector('.orderFilter').value;
        let urlParams = new URLSearchParams();
        if (order || ship) {
            urlParams.set('ShipMonth', ship);
            urlParams.set('OrderMonth', order);
            window.location.href = "/order/filter?"+urlParams.toString();
        }
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

const addOrder = document.querySelector('.btn-add');
const addOrderForm = document.querySelector('.add-order-form');
if (addOrder) {
    addOrder.addEventListener('click', function () {
        addOrderForm.classList.remove('d-none');
    });
}

const closeForm = document.querySelector('.btn-close');
if (closeForm) {
    closeForm.addEventListener('click', function () {
        addOrderForm.classList.add('d-none');
    });
}