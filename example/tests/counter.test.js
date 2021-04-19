var assert = require("assert");

var codePath = "../counter/counter.py";

var lang = "py"
var type = "native"
function deploy() {
    return xchain.Deploy({
        name: "counter",
        code: codePath,
        lang: lang,
        type: type,
        init_args: { "creator": "xchain" },
        options: { "account": "xchain" }
    });
}
//
Test("Increase", function (t) {
    var c = deploy();

    var resp = c.Invoke("Increase", { "key": "key" });
    console.log(resp.Message)
    console.log(resp.Body)
    assert.equal(resp.Body, "1");
    var resp = c.Invoke("Get", { "key": "key" })
    assert.equal(resp.Body, "1")
})

Test("Delete", function (t) {
    var c = deploy()

    var resp = c.Invoke("Get", { "key": "xchain" })
    assert.equal(resp.Status, 500)

    c.Invoke("Increase", { "key": "xchain" })
    resp = c.Invoke("Get", { "key": "xchain" })
    assert.equal(resp.Status, 200)

    c.Invoke("Delete", { "key": "xchain" })
    resp = c.Invoke("Get", { "key": "xchain" })
    assert.equal(resp.Status, 500)
})
