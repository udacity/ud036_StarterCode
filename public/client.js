// client-side js
// run by the browser each time your view template is loaded

// by default, you've got jQuery,
// add other scripts at the bottom of index.html

$(function() {
  console.log('hello world :o');
  
   // Pause the video when the modal is closed
  $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
      // Remove the src so the player itself gets removed, as this is the only
      // reliable way to ensure the video stops playing in IE
      $("#trailer-video-container").empty();
  });
  // Start playing the video whenever the trailer modal is opened
  $(document).on('click', '.movie-tile', function (event) {
      var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
      var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
      $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
      }));
  });
  // Animate in the movies when the page loads
  $(document).ready(function () {
    $('.movie-tile').hide().first().show("fast", function showNext() {
      $(this).next("div").show("fast", showNext);
    });
  });
  /*
  $.get('/dreams', function(dreams) {
    dreams.forEach(function(dream) {
      $('<li></li>').text(dream).appendTo('ul#dreams');
    });
  });

  $('form').submit(function(event) {
    event.preventDefault();
    var dream = $('input').val();
    $.post('/dreams?' + $.param({dream: dream}), function() {
      $('<li></li>').text(dream).appendTo('ul#dreams');
      $('input').val('');
      $('input').focus();
    });
  });*/

});


var navMenu;
var productInfo = [];
const imgDIR = '/images/products/';
const INITIAL_QUANTITY = 5;
const INAVTIVITY_TIME_LIMIT = 30;

console.log('IMPORTANT: Please run the command "npm install" and ' +
    'then "heroku local web" in the source directory');

// GET request to get navigation menu items from the server and call navMenuController function
httpGetAsync('/navMenuList', navMenuController);

// GET request to get product items from the server and call productListController function
httpGetAsync('/productList', productListController);

// Adding on click listener to showCart button
addShowCartListener();

// Adding on window load listener to start inactiveTimer
addStartTimerListener();


/*
 * MVC design pattern
 * This design pattern makes sure there is no direct connection between
 * model(app data) and the view (rendered content/ DOM)
 * This allows the ease of changing model/view without affecting the other
 */

/***********************************************************************************************************************
 *              MODEL
 **********************************************************************************************************************/

var products = [];
var cart = [];
var inactiveTime = 0;

/**
 * reset inactiveTime variable
 */
function resetTimer() {
    inactiveTime = 0;
}

/**
 * inActive Timer functionality
 */
function startTimer() {
    if (inactiveTime >= INAVTIVITY_TIME_LIMIT) {
		// Inactive for 30 seconds
        alert("Hey there! Are you still planning to buy something?");
        resetTimer();
        startTimer();
    } else {
		// 1 second yield to the function below
        setTimeout(function () {
            var inactiveTimeDisplay = document.getElementById("inactiveTimeDisplay");
            inactiveTimeDisplay.innerHTML = ++inactiveTime + " seconds";
            startTimer();
        }, 1000);
    }
}


/**
 * Push another productInfo element
 * @param name      - stores name of the product
 * @param quantity  - stores quantity of the product left in store
 * @param cost      - stores cost of the product
 */
function addProductInfo(name, quantity, cost) {
    productInfo[name] = {
        quantity: quantity,
        cost: cost
    };
}

/**
 * Push another element into Products Array
 * @param name      - stores name of the product
 * @param quantity  - stores quantity of the product left in store
 */
function addProduct(name, quantity) {
    products[name] = quantity;
}

/**
 * Convert array (inside a string )to actual JavaScript array
 * Reason: response from back-end is in the form of string.
 *          Evem an array returned from back-end is inside a string.
 *          TODO: Look into how to recieve an actual array
 * @param str - contains the array in string form
 */
function stringToArray(str) {
    return JSON.parse("[" + str + "]");
}

/**
 * Sets navMenu array containing array of all navMenu items
 * @param       - navMenuList navMenu list recieved from backend in string form
 * @returns {*} - for debugging purposes
 */
function setNavMenu(navMenuList) {
    navMenu = stringToArray(navMenuList);
    return navMenu;
}

/**
 * Sets product list information in products and productInfo arrays
 * @param productList - Array of products recieved from back-end in string form
 * @returns {Array} - List of product in JavaScript Array form
 */
function initializeProductList(productList) {
    var temp = stringToArray(productList);

    temp[0].forEach(function (product) {
        var pName = product.split('_')[0];
        var pQuantity = INITIAL_QUANTITY;
        var pCost = product.split('_')[1];

        addProductInfo(pName, pQuantity, pCost);
        addProduct(pName, pQuantity);               // only for assignment-2
    });
    return products;
}

/**
 * Checks if product with the name pName is in the cart
 * @param pName         - name of the product being checked in cart
 * @returns {boolean}   - true if the product is in the cart, false otherwise
 */
function productInCart(pName) {
    return !(cart[pName] === undefined);
}

/**
 * Decrement the number of products by the name pName from the store
 * @param pName - name of the product being added to cart
 */
function decreaseStock(pName) {
    --productInfo[pName]['quantity'];
    --products[pName];
}

/**
 * Increment the number of products by the name pName in the store
 * @param pName - product name
 */
function addProductToCart(pName){
    ++cart[pName];
}

/**
 * Increment the number of products by the name pName in the store
 * @param pName - name of the product being removed from cart
 */
function increaseStock(pName) {
    ++productInfo[pName]['quantity'];
    ++products[pName];
}

/**
 * Decrement the number of product by the name pName in the store
 * @param pName - product name
 */
function removeProductFromCart(pName){
    delete cart[pName];
}

/***********************************************************************************************************************
 *              CONTROLLER
 **********************************************************************************************************************/

/**
 * Add on load listener to start the timer when the window has loaded
 */
function addStartTimerListener() {
    window.onload = startTimer;
}

/**
 * Add on click listener to show cart when the cart button is clicked
 */
function addShowCartListener(){
    document.getElementById('showCartButton').onclick = showCart;
}

/**
 * On click listener to add a product to cart when Add button is clicked
 * @param productName - name of the product being added to the cart
 */
function addToCart(productName) {
    resetTimer();
    if (productInfo[productName]['quantity'] <= 0) {
        // Out of stock
    } else {
        if (!productInCart(productName)) {
            cart[productName] = 1; // Initializing the product in cart array
        } else {
            addProductToCart(productName); //model function
        }
        decreaseStock(productName); //model function
    }
}

/**
 * On click listener to remove a product from cart when Remove button is clicked
 * @param productName - name of the product being removed from cart
 */
function removeFromCart(productName) {
    resetTimer();
    if (!productInCart(productName)) {
        // already 0!
        alert(productName + ' does not exist in the cart!');
    } else {
        increaseStock(productName);             // model function
        if (--cart[productName] === 0) {
            removeProductFromCart(productName); // model function
        }
    }
}

/**
 * Show the cart as an alert message
 */
function showCart() {
    var cartContent = '';
    var cartLength = Object.keys(cart).length; // to get length of an associative array (cart.length === 0)
    if (cartLength > 0) {
        for (var product in cart) {
            cartContent += product + ' : ' + cart[product] + '\n';
        }
    } else {
        cartContent = "Nothing in cart!";
    }
    alert(cartContent);
}

/**
 * Asynchronous GET request
 * @param theUrl    - url of the request
 * @param callback  - callback function for the request
 */
function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
            callback(xmlHttp.response);
    };
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

/**
 * Controller function for Navigation Menu
 * Callback function that recieves navMenu list from back-end
 * @param navMenuList
 */
function navMenuController(navMenuList) {
    setNavMenu(navMenuList);    // model function
    renderNavMenu();            // view function
}

/**
 * Controller function for product list
 * Callback function that recieves product list from back-end
 * @param navMenuList
 */
function productListController(productList) {
    initializeProductList(productList); // model function
    renderProductList();                // view function
}

/***********************************************************************************************************************
 *              VIEW
 **********************************************************************************************************************/

/**
 * renders Navigation Menu
 */
function renderNavMenu() {
    navMenu[0].forEach(function (menuItem) {

        //Create each navMenu DOM element
        var navButton = document.createElement('li');
        navButton.className = 'navMenuButton';
        navButton.id = menuItem;
        navButton.innerHTML = menuItem;

        //Append it to the navMenu
        var menu = document.getElementById('navigationMenu');
        menu.appendChild(navButton);
    });
}


/**
 * Helper function to create DOM elements
 * @param   {string}  tagName       - HTML tag name (e.g. div, li, span, etc)
 * @param   {JSON}    attrArray     - list of attributes for the new DOM element
 * @returns {Element} newNode       - the new DOM element created
 */
function createNewNode(tagName, attrArray) {
    var newNode = document.createElement(tagName);
    var keys = Object.keys(attrArray);

    // iterates through all atrributes to be given to the new DOM element
    for (var i = 0; i < keys.length; i++) {
        switch (keys[i]) {
            case 'class':       newNode.className = attrArray[keys[i]]; break;
            case 'id':          newNode.id = attrArray[keys[i]];        break;
            case 'src':         newNode.src = attrArray[keys[i]];       break;
            case 'innerHTML':   newNode.innerHTML = attrArray[keys[i]]; break;
            default:            console.log('weird: ' + keys[i]);
        }
    }
    return newNode;
}

/*
 * Structure for a product div:
 *
 *   product div
 *       - image
 *       - name
 *       - overlay2
 *           - cost
 *           - border shadow
 *       - overlay
 *           - cart image
 *           - add button
 *           - remove button
 */

/**
 * Renders the products
 */
function renderProductList() {

    for (var product in products) {
        var pDiv        = createNewNode('div',{'class':'col-3 col-m-3 productDiv', 'id':product});
        var pImage      = createNewNode('img',{'class':'productImg','src':imgDIR+product+'_' + productInfo[product]['cost']+'.png'});
        var pName       = createNewNode('div',{'class':'col-12 col-m-12 productNameDiv','innerHTML':product});
        var overlayDiv2 = createNewNode('div',{'class':'overlay2'});
        var pCost       = createNewNode('div',{'class':'col-12 col-m-12 productCostDiv','innerHTML': productInfo[product]['cost']});
        var overlayDiv  = createNewNode('div',{'class':'overlay'});
        var cartImg     = createNewNode('img',{'class':'cartImg','src':'images/cart.png'});
        var addButton   = createNewNode('button',{'class':'col-5 col-m-5 addToCartButton','innerHTML':'Add'});
        var removeButton = createNewNode('button',{'class': 'col-5 col-m-5 removeFromCartButton','innerHTML': 'Remove'});

        addButton.onclick = function () {
            // TODO: move this to controller
            var productName = this.parentElement.parentElement.id;
            addToCart(productName);
        };

        removeButton.onclick = function () {
            // TODO: move this to controller
            var productName = this.parentElement.parentElement.id;
            removeFromCart(productName);
        };

        pDiv.appendChild(pImage);
        pDiv.appendChild(pName);
        overlayDiv2.appendChild(pCost);
        pDiv.appendChild(overlayDiv2);
        overlayDiv.appendChild(cartImg);
        overlayDiv.appendChild(addButton);
        overlayDiv.appendChild(removeButton);
        pDiv.appendChild(overlayDiv);

        var productDisplayArea = document.getElementById('productList');
        productDisplayArea.appendChild(pDiv);
    }
}