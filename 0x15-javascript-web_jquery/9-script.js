/**
 * This script fetches from a URL
 */
$(document).ready(() => {
    $.ajax({
        url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
        success: (result) => {
            $('DIV#hello').text(result.hello);
        },
    });
});
