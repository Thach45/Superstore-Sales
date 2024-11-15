formSearch = document.querySelector('.form-Search');

let sortElement = document.querySelector('.btn-sort'); // Giả sử phần tử sort có class là 'sort-element'
let sortAscending = true; // Biến để theo dõi trạng thái hiện tại
const filterCategory = document.querySelector('.categoryFilter');
const filterSub = document.querySelector('.subFilter');

const applyFilter = document.querySelector('#applyFilters');
//chức năng tìm kiếm

//chức năng sort

//chức năng filter
if (applyFilter) {
    applyFilter.addEventListener('click', function () {
        let category = filterCategory.value;
        let sub = filterSub.value;
        window.location.href = '/product/filter?Category=' + category + '&Sub-Category=' + sub;
       
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