document.addEventListener('DOMContentLoaded', function() {   
  const MyList = document.querySelector('#My-List')
  let Page =  ['write']
  let button1 = document.createElement("button")
  button1.textContent = 'Check page'
  button1.className = "fir_st"
  let button2 = document.createElement("button")
  button2.textContent = 'Add Page'
  button2.className = "sec_ond"
  document.querySelectorAll("#My-List li").forEach(eLI=>eLI.appendChild(button1.cloneNode(true)))
  document.querySelectorAll("#My-List li").forEach(eLI=>eLI.appendChild(button2.cloneNode(true)))
  document.querySelector('#My-List').onmouseover = function() {
    var view1 = document.getElementsByClassName('fir_st');
    for (var i=0; i<view1.length; i++) {
    if(view1[i].style.visibility == 'hidden'){
                  // do some stuff
       view1[i].style.visibility = 'visible'
      }
        else{
                 // do some stuff
               view1[i].style.visibility = 'visible'
            }
     } 

     document.querySelector('#My-List').onmouseout = function() {
      var view1 = document.getElementsByClassName('fir_st');
      for (var i=0; i<view1.length; i++) {
      if(view1[i].style.visibility == 'visible'){
                    // do some stuff
         view1[i].style.visibility = 'hidden'
         }
           else{
                   // do some stuff
                 view1[i].style.visibility = 'hidden'
              }
       } 

      var view2 = document.getElementsByClassName('sec_ond');
      for (var i=0; i<view2.length; i++) {
      if(view2[i].style.visibility == 'visible'){
                // do some stuff
         view2[i].style.visibility = 'hidden'
      }
       else{
               // do some stuff
             view2[i].style.visibility = 'hidden'
           }
       } 
    }

    var view2 = document.getElementsByClassName('sec_ond');
    for (var i=0; i<view2.length; i++) {
    if(view2[i].style.visibility == 'hidden'){
              // do some stuff
       view2[i].style.visibility = 'visible'
    }
     else{
             // do some stuff
           view2[i].style.visibility = 'visible'
         }
     } 
  }
  document.querySelector('#My-List').onclick = function() {
    if (event.target.className =='fir_st') {
    let pLI = event.target.parentElement
    //var z = document.createElement('p')
   // z.innerHTML = Page + pLI.toString()
    //k.appendChild("bad")
    Page.push(pLI)
    document.querySelector('h3').innerHTML = Page

    
    }

    if (event.target.className =='sec_ond') {
    let pLI = event.target.parentElement
    MyList.removeChild(pLI)

    }

  }  
  
})

export { Page };