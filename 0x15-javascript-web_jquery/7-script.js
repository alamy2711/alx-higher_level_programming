/**
 * This script that fetches the character name from the URL
 */
$.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: (result) => {
        $('DIV#character').text(result.name);
    },
});
