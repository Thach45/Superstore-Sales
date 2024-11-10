formSearch = document.querySelector('.form-Search');

let sortElement = document.querySelector('.btn-sort'); // Giả sử phần tử sort có class là 'sort-element'
let sortAscending = true; // Biến để theo dõi trạng thái hiện tại
if (formSearch) {
    formSearch.addEventListener('submit', function (e) {
        e.preventDefault();
        let search = document.querySelector('.search').value;
        
        if (search) {
            if (search[2] =="-") {
                window.location.href = '/search?IDCustomer=' + encodeURIComponent(search);
            }
            else
                window.location.href = '/search?Name=' + encodeURIComponent(search);
        } else {
            window.location.href = '/';
        }
    });
}
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
            window.location.href = '/sort?sort=' + sortElement.name; // Chuyển hướng trang với tham số sort
        }
    });
}

