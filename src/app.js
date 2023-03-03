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

    let firstName = document.getElementById("fname");
    let lastName = document.getElementById("lname");
    let major = document.getElementById("major");
    let resume = document.getElementById("resume");
    let jsonData = document.getElementById("jsontext");

    if (firstName.value == "" || lastName.value == "" || major.value == "" || resume.value == "") {
        alert("MISSING REQUIRED FIELDS");
    }
    else {
        alert("This form has been successfully submitted");
        console.log(
            "User: " + firstName.value + " " + lastName.value + "\n" +
            "Major: " + major.value + "\n" +
            "Resume Text: \n" +  resume.value);
    }

    // const fs = require('fs');
    // let filename = firstName.value + "_" + lastName.value + "_" + major.value + ".txt";
    // fs.writeFile(filename, resume.value, (err) => {
    //     if (err) throw err;
    //     else {
    //         console.log("File successfully saved");
    //     }
    // });
    

    firstName.value = "";
    lastName.value = "";
    major.value = "";
    resume.value = "";
});