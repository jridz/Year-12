// Inefficient: Memory leak from event listeners

function addButtons() {

    const button = document.createElement( 'button' );

    button.textContent = "Click Me" ;

    document.body.appendChild(button);



    // Event listener added

    button.addEventListener('click', () => {

        console.log( "Button clicked!" );

    });



    // If button is removed, event listener stays in memory

    document.body.removeChild(button);

}

addButtons();



// Efficient: Remove event listener before deleting

function addAndCleanButtons() {

    const button = document.createElement( 'button' );

    button.textContent = "Click Me" ;

    document.body.appendChild(button);



    function handleClick() {

        console.log( "Button clicked!" );

    }



    button.addEventListener( 'click' , handleClick);



    // Remove event listener before deletion

    button.removeEventListener('click', handleClick);

    document.body.removeChild(button);

}

addAndCleanButtons();