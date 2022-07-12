function show_1() {
    document.getElementById('e1').innerHTML = [
        "<span>GET: /api</span>",
        "<span>GET: /api/[currency]</span>",
        "<span>GET: /api/[currency]/[city]/[place]</span>"].join('<br>');
}