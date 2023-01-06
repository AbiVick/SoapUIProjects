
// variable 

//Array in javascript

let superHero = ['SuperMan', 'Hulk', 'Capt AMerica', 'Thor', 'Sp.Man', 23423, 234234.32423, true]
console.log(superHero.length);
console.log(superHero[3]);
console.log(superHero[superHero.length   - 1 ]);

// function in javascript 
// ''
// ""
// ``   --- tick  below the escape key

function greeting(name='Amit Pratap'){

    console.log("hello " + name + ", welcome you in  today session, my fav superHero are:  " + superHero[0])

    console.log(`hello  ${name}  welcome you in  today session, my fav superHero are:   ${superHero[0]}`)

}

greeting('Dinesh Kartik')

greeting()

//=======================================================================================================
