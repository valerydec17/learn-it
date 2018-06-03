// // EXAMINE THE DOCUMENT OBJECT //

// console.dir(document);
// console.log(document.URL);
// console.log(document.title);
// document.title = 123;
// console.log('Hi');

// console.log(document.doctype);
// console.log(document.head);
// console.log(document.body);
// console.log('All in DOM');
// console.log(document.all);

// console.log(document.forms);
// console.log(document.links);

// console.log(document.getElementById('header-title'));

// var headerTitle = document.getElementById('header-title');
// var header = document.getElementById('main-header'); 
// console.log(headerTitle);
// headerTitle.textContent = 'Hello';
// //headerTitle.innerText = 'GoodBye';

// header.style.borderBottom = 'solid 15px #000'; 

// var items = document.getElementsByClassName('list-group-item');
// console.log(items);
// console.log(items[2]);
// items[2].textContent = 'Hello3';
// items[2].style.backgroundColor = 'green';

// for(var i = 0; i < items.length; i++){
// 	items[i].style.backgroundColor = '#f4f4f4';
// }


// var li = document.getElementsByTagName('li');
// console.log(li);
// console.log(li[1]);
// li[1].textContent = 'Hello3';
// li[1].style.backgroundColor = 'green';

// for(var i = 0; i < li.length; i++){
// 	li[i].style.backgroundColor = '#f4f4f4';
// }

var item =  document.querySelector('.list-group-item');
item.style.color = 'red';

var lastItem = document.querySelector('.list-group-item:last-child');
lastItem.style.color = 'blue';

var secondItem = document.querySelector('.list-group-item:nth-child(2)');
secondItem.style.color = 'coral';



var odd = document.querySelectorAll('li:nth-child(odd)');
var even = document.querySelectorAll('li:nth-child(even)');

for(var i = 0; i < odd.length; i++){
	odd[i].style.backgroundColor = '#f4f4f4';
	even[i].style.backgroundColor = '#ccc';
}

