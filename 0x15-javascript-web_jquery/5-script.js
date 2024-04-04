/**
 * This script that adds a <li> element to a list
 */
$('DIV#add_item').click(() => {
    $('ul.my_list').append('<li>Item</li>');
});
