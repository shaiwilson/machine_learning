$(function (){ 

    function addToFavorites(evt){

        var id = this.id; 

        $.post("/add-to-favorites", {'id': id}, addToFavoritesSuccess);
    }

    function addToFavoritesSuccess(result){

        console.log(result.status);

        var id = result.id;

        $('#' + id).css('color', 'red'); 
    }

    $('.favorite-btn').click(addToFavorites);

}) 