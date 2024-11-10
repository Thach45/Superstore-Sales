formSearch = document.querySelector('.form-Search');

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