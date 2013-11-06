$('#query').on("keypress", function(t) {
    var XFIRE_ROOT = "http://www.xfire.com/users/";
    var YQL_API = 'http://query.yahooapis.com/v1/public/yql?q=';
    var YQL_CSS = "'http://yqlblog.net/samples/data.html.cssselect.xml' as data.html.cssselect ";
    if (13 == t.keyCode) {
        $("div.progress").toggleClass("hidden active");

        username = $('#query').val();
        console.log(username);
        $('#result').text(username);

        /* http://query.yahooapis.com/v1/public/yql?q=use%20'http%3A%2F%2Fyqlblog.net%2Fsamples%2Fdata.html.cssselect.xml'%20as%20data.html.cssselect%3B%0Aselect%20*%20from%20data.html.cssselect%20where%20url%3D%22http%3A%2F%2Fwww.xfire.com%2Fusers%2Fpathway2727%22%20and%20css%3D%22%23template_container%20.games%22&format=json&diagnostics=true&callback=
           http://query.yahooapis.com/v1/public/yql?q=use%20'http%3A%2F%2Fyqlblog.net%2Fsamples%2Fdata.html.cssselect.xml'%20as%20data.html.cssselectselect%20*%20from%20data.html.cssselect%20where%20url%3D%22http%3A%2F%2Fwww.xfire.com%2Fusers%2Fpathway27%22and%20css%3D%22%23template_container%20.games%22
*/
        var YQL_QUERY = encodeURI(YQL_API) + encodeURIComponent('use ' + YQL_CSS +
                                           'select * from data.html.cssselect where url="' +
                                           XFIRE_ROOT + username + '"' +
                                           'and css="#template_container table"') + 
                                           encodeURI('&format=xml&callback=')

        // GET THE TYPE U WILL USE AS
        var stuff = $.get( YQL_QUERY, cbFunc , "html");
        console.log(YQL_QUERY);
        function cbFunc(data) {
            console.log(data);
            info = $(data).find('table');
            console.log(info);

            $('#results').html(info);
            clean_table();
            //var obj = jQuery.parseJSON(data);
            //console.log(data.query.results.results.table);

            $("div.progress").toggleClass("hidden active");
        }


        /*
         * XML
         * http://query.yahooapis.com/v1/public/yql?q=use%20'http%3A%2F%2Fyqlblog.net%2Fsamples%2Fdata.html.cssselect.xml'%20as%20data.html.cssselect%3B%0Aselect%20*%20from%20data.html.cssselect%20where%20url%3D%22http%3A%2F%2Fwww.xfire.com%2Fusers%2Fpathway2727%22%20and%20css%3D%22%23template_container%20.games%22&diagnostics=true
         *
         * JSON
        */

    }
})


function clean_table() {
    $('table').toggleClass("games table")
    $('tr').unwrap()
    $('tr:first').wrap("<thead></thead>");
    $('tr:gt(0)').wrapAll('<tbody class="list"></tbody>');

    // Get rid of paragraphs
    $('table p').contents().unwrap();

    //$('tr:first th').each(function (index) {
    //    $(this).toggleClass($(this).text());
    //});

    //$('tr:first').unwrap();
    //table = $('tr').wrapAll('<table class="table"></table>');


}
