$(document).ready(function() {
    $('#users').DataTable({
        ajax: {
            url : "http://localhost:3000/users",
            type : "GET",
            dataSrc : ""
        },
        columns: [
            { data : "Name" },
            { data : "Address" },
            { data : "Sanction Type" },
            { data : "Other Name/Logo" },
            { data : "Nationality" },
            { data : "Effect Date | Lapse Date" },
            { data : "Grounds" }
        ]
    } );
});
