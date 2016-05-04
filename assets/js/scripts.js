function check1() {
    with(document.all) {
        if (input1.value != input2.value) {
            alert("两次输入密码不同")
            input1.value = "";
            input2.value = "";
        } else document.forms[0].submit();
    }
}

function check2() {
    with(document.all) {
        if (input3.value != input4.value) {
            alert("两次输入密码不同")
            input3.value = "";
            input4.value = "";
        } else document.forms[0].submit();
    }
}
var field1;
var field2;
var field3;
var field4;
var field5;
var field6;
var field7;
var field8;
var field9;
var field0;

function modify(ida) { //web display control function
    id = "#" + ida;

    field1 = $(id).children("td").eq(0);
    field2 = $(id).children("td").eq(1);
    field3 = $(id).children("td").eq(2);
    field4 = $(id).children("td").eq(3);
    field5 = $(id).children("td").eq(4);

    $(id).html("<form id=\""+ida+"f\" class=\"form-inline\" action=\"ModifyListItem\" method=\"post\" role=\"form\"><td style=\"display:none;\"><input style=\"display:none;\" form=\""+ida+"f\" type=\"text\" name=\"ID\" class=\"form-modify\" value=\""+field1.text()+"\"></td><td><input form=\""+ida+"f\" type=\"text\" name=\"bookName\" class=\"form-modify\" value=\""+field2.text()+"\"></td><td><input form=\""+ida+"f\" type=\"text\" name=\"bookAuthor\" class=\"form-modify\" value=\""+field3.text()+"\"></td><td><input form=\""+ida+"f\" type=\"text\" name=\"bookClass\" class=\"form-modify\" value=\""+field4.text()+"\"></td><td><input form=\""+ida+"f\" type=\"text\" name=\"status\" class=\"form-modify\" value=\""+field5.text()+"\"></td><td><a onclick=\"undo('"+ida+"')\">撤销</a><input form=\""+ida+"f\" type=\"submit\" value=\"提交\" class=\"btn btn-link\"></td></form>");

}

function undo(ida) {
    id = "#" + ida;
    $(id).html("<form action=\"DeleteListItem\" id=\"t"+ida+"d\" onsubmit=\"get_lid('t"+ida+"')\" class=\"form-inline\"><input form=\"t"+ida+"d\" id=\"t"+ida+"i\" type=\"hidden\" name=\"ID\" value=\"\"></form><td style=\"display:none;\">"+field1.text()+"</td><td>"+field2.text()+"</td><td>"+field3.text()+"</td><td>"+field4.text()+"</td><td>"+field5.text()+"</td><td><a onclick=\"modify('"+ida+"')\">修改</a><input form=\"t"+ida+"d\" type=\"submit\" value=\"删除\" class=\"btn btn-link\"></td>");
}

function modifyplan(ida) { //web display control function
    id = "#" + ida;

    field6 = $(id).children("div").children("a").eq(0);
    field7 = $(id).children("div").eq(1).children("div").children("dl").children("dd").eq(0);
    field8 = $(id).children("div").eq(1).children("div").children("dl").children("dd").eq(1);
    field9 = $(id).children("div").eq(1).children("div").children("dl").children("dd").eq(2);
    field0 = $(id).children("div").eq(1).children("div").children("dl").children("dd").eq(3);


    $(id).html("<div class=\"panel-heading\"><a class=\"panel-title\" data-toggle=\"collapse\" data-parent=\"#panel-101092\" href=\"#panel-element-413777\"><input name=\"planTime\" form=\""+ida+"f\"value=\""+$.trim(field6.text())+"\"></a><a class=\"btn-right\" onclick=\"undoplan('"+ida+"')\">撤销</a></div><div id=\"panel-element-413777\" class=\"panel-collapse collapse\"><div class=\"panel-body\"><form id=\""+ida+"f\" class=\"form-horizontal\" method=\"post\" action=\"ModifyPlanItem\" role=\"form\"><dl class=\"dl-horizontal\"><dt>书名</dt><dd><input value=\""+$.trim(field7.text())+"\" type=\"text\" form=\""+ida+"f\" name=\"bookName\"></dd><dt>进度</dt><dd><input value=\""+$.trim(field8.text())+"\" type=\"text\" form=\""+ida+"f\" name=\"status\"></dd><dt style=\"display:none;\">ID</dt><dd style=\"display:none;\"><input name=\"ID\" value=\""+$.trim(field0.text())+"\" type=\"text\" form=\""+ida+"f\" name=\"status\"></dd><dt>感想</dt><dd><textarea id=\""+ida+"t\" form=\""+ida+"f\" cols=\"60\" rows=\"5\" form=\"p1f\" name=\"thoughts\"></textarea></dd><dt></dt><dd><input type=\"submit\" form=\""+ida+"f\" value=\"提交\" class=\"btn btn-link\"></dd></dl> </form></div></div>");

}

function undoplan(ida) {
    id = "#" + ida;
    $(id).html("<div class=\"panel-heading\"><a class=\"panel-title\" data-toggle=\"collapse\" data-parent=\"#panel-101092\" href=\"#panel-element-31581\">"+field6.text()+"</a><a class=\"btn-right\" onclick=\"modifyplan('"+ida+"')\">修改</a></div><div id=\"panel-element-31581\" class=\"panel-collapse collapse in\"><div class=\"panel-body\"><dl class=\"dl-horizontal\"><dt>书名</dt><dd>"+field7.text()+"</dd><dt>进度</dt><dd>"+field8.text()+"</dd><dt>感想</dt><dd>"+field9.text()+"</dd></dl></div></div></div>")
}

function get_lid(ida){
    id = "#" + ida;
    field1 = $(id).children("td").eq(0);
    $(id+"i").val(field1.text());
}

function get_pid(ida){
    id = "#" + ida;
    field0 = $(id).children("div").eq(1).children("div").children("dl").children("dd").eq(3);
    $(id+"i").val(field0.text());
}