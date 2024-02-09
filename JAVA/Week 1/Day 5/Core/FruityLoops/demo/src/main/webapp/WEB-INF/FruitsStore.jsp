<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <!-- New line below to use the JSP Standard Tag Library -->
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Fruits Store</title>
    </head>
<body>
    <h1>Fruits Store</h1>
    
    <table border="1">
        <thead>
            <tr>
                <th>Fruit Name</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <c:forEach items="${fruits}" var="oneFruit">
                <tr>
                    <td>${oneFruit.name}</td>
                    <td>${oneFruit.price}</td>
                </tr>
            </c:forEach>
        </tbody>
    </table>
</body>
</html>
