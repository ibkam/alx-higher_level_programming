// script that adds a <li> element
$('DIV#add_item').click(() => {
  $('UL.my_list').append('<li>Item</li>');
});
