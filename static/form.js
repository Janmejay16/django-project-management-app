function assignClass() {

    var hlprs = document.querySelectorAll(".helptext");
    for (const hlpr of hlprs) {
        hlpr.className = 'alert alert-info'
    }

    var divs = document.querySelectorAll("form div");
    for (const div of divs) {
        if (div.className !== 'alert alert-info')
            div.className = 'form-group'
    }

    var ipts = document.querySelectorAll("input");
    for (const ip of ipts) {
        ip.className = 'form-control'
    }

    var txtareas = document.querySelectorAll('textarea')
    for (const i of txtareas) {
        i.rows = 5
    }

    var slcts = document.querySelectorAll("select");
    for (const s of slcts) {
        s.className = 'form-control'
    }

    var forms = document.getElementsByTagName("form")
    for (const form of forms) {
        form.className = 'card'
    }

    var inputBtns = document.querySelectorAll("form input[type='submit']")
    for (const btn of inputBtns) {
        btn.className = 'btn-primary rounded p-2'
    }
}