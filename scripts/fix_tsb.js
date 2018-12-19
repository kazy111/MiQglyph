var fs = require('fs');
var height = 840;
// read
var content = fs.readFileSync('MiQglyph.ttx', 'utf8').split(/\r\n/);

// fix top side bearing
var pattern = /    <mtx name="([^"]+)" height="([\-0-9]+)" tsb="([\-0-9]+)"\/>/;
var result = '';
for (var line of content) {
    var matches = line.match(pattern);
    if (matches) {
        var id = matches[1];
        var em_height = matches[2];
        var tsb = parseInt(matches[3]);
        switch (id){
            case '.notdef':
                tsb = 50;
                break;
            case 'uni3041':
            case 'uni3043':
            case 'uni3045':
            case 'uni3047':
            case 'uni3049':
            case 'uni3063':
            case 'uni3083':
            case 'uni3085':
            case 'uni3087':
            case 'uni30A1':
            case 'uni30A3':
            case 'uni30A5':
            case 'uni30A7':
            case 'uni30A9':
            case 'uni30C3':
            case 'uni30E3':
            case 'uni30E5':
            case 'uni30E7':
                tsb = height - tsb - 250;
                break;
            default:
                tsb = height - tsb;
        }
        result += '    <mtx name="' + id + '" height="' + em_height + '" tsb="' + tsb.toString() + '"/>\r\n';
    } else {
        result += line + '\r\n';
    }
}

// write
fs.writeFileSync('MiQglyph.ttx', result);

