
$('button').click(function() {
    var query = $('#query').val();

    axios.get('/cbv/search_book_by_get_method/', {
        params: {
            query: query,
        }
    })
    .then(function (response) {
        // console.log(response.data);

        for (i in response.data) {
            console.log(response.data[i])
            $('p').append(response.data[i]);
        }
    })
    .catch(function (error) {
        console.log(error);
    })
})
