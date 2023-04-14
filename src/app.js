'use strict';
const switcher = document.querySelector('.btn');
switcher.addEventListener('click', function() {
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');
    const className = document.body.className;
    if(className == "light-theme") {
        this.textContent = "Dark";
    } else {
        this.textContent = "Light";
    }
});

let userDataForm = document.getElementById("userInfo");
userDataForm.addEventListener("submit", (e) => {
    e.preventDefault();

    let firstName = document.getElementsByName("fname");
    let lastName = document.getElementsByName("lname");
    let major = document.getElementsByName("major");
    let resume = document.getElementById("resume").files[0];

    // if (firstName.value == undefined || lastName.value == undefined || major.value == undefined) {
    //     alert("MISSING REQUIRED FIELDS");
    // }
    //else 
    {
        alert("This form has been successfully submitted");
        console.log(
            "User: " + firstName.value + " " + lastName.value + "\n" +
            "Major: " + major.value + "\n" + resume);
        // firstName.value = "";
        // lastName.value = "";
        // major.value = "";
        // resume = null;
        window.location.reload();
    }

    // const fs = require('fs');
    // let filename = firstName.value + "_" + lastName.value + "_" + major.value + ".txt";
    // fs.writeFile(filename, resume.value, (err) => {
    //     if (err) throw err;
    //     else {
    //         console.log("File successfully saved");
    //     }
    // });
    
});

// let contactForm = document.getElementById("contactSheet");
// contactForm.addEventListener("submit", (e) => {
//     e.preventDefault();

//     let name = document.getElementById("name");
//     let email = document.getElementById("email");
//     let concern = document.getElementById("cocern");


//     if (name.value == "" || email.value == "" || concern.value == "") {
//         alert("MISSING REQUIRED FIELDS");
//     }
//     else if (concern.value.includes("@") != true) {
//         alert("INVALID EMAIL")
//     }
//     else {
//         alert("This form has been successfully submitted");
//         console.log(
//             "Name: " + name.value + "\n" +
//             "Email: " + major.value + "\n" +
//             "Concern: \n" +  concern.value);
//         name.value = "";
//         email.vakue = "";
//         concern.value = "";
//     }

//     // const fs = require('fs');
//     // let filename = firstName.value + "_" + lastName.value + "_" + major.value + ".txt";
//     // fs.writeFile(filename, resume.value, (err) => {
//     //     if (err) throw err;
//     //     else {
//     //         console.log("File successfully saved");
//     //     }
//     // });
    

    
// });