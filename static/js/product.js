
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