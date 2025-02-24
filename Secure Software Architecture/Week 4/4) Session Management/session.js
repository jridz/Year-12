

const itemInput = document.getElementById('itemInput');

const addItemButton = document.getElementById('addItemButton');

const cart = document.getElementById('cart');



// Load items from localStorage

const savedCart = JSON.parse(localStorage.getItem('cart')) || [];

savedCart.forEach(item => addItemToCart(item));



// Add item to cart and save to localStorage

addItemButton.addEventListener('click', function() {
    // Remove leading & trailing whitespace from user input

    const item = itemInput.value.trim();

    if (item) {

        addItemToCart(item);



        // Save updated cart to localStorage

        // Add item to end of savedCart array

        savedCart.push(item);

        // Save updated savedCart as a string

        localStorage.setItem('cart', JSON.stringify(savedCart));



        // Save current cart size to sessionStorage

        //  cartSize is the sessionStorage key

        sessionStorage.setItem('cartSize', savedCart.length);



        // clear the input field

        itemInput.value = '';

    }

});



function addItemToCart(item) {

    // Create a new list element

    const listItem = document.createElement('li');


    listItem.textContent = item;

    cart.appendChild(listItem);

}



// Clear cart size when session ends

window.addEventListener('beforeunload', function() {

    sessionStorage.removeItem('cartSize');

});

