<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<% String ans =(String)request.getAttribute("ans"); %>

<h2><%= ans %></h2>
<br>
<form method="get" name="final" action="raj_hw1.jsp">
<button type="submit" name="button">Home</button>
</form>
</body>
</html>