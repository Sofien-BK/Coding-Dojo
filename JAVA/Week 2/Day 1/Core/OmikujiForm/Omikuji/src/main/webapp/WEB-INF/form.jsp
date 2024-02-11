<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <!-- New line below to use the JSP Standard Tag Library -->
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Demo JSP</title>
    </head>
<body>
    <h1>Send an Omikuji!</h1>
    
    <form action="/omikuji/processOmikuji" method="POST">
    
    <label>Pick Any Number From 5 To 25</label>
    <input name="number" type="number" min="5" max="25">
    <br>
    <label>Enter The Name Of Any City</label>
    <input name="city">
    <br>
    <label>Enter The Name Of Any Real Person</label>
    <input name="person">
    <br>
    <label>Enter Professional Endeavor Or Hobby</label>
    <input name="hobby">
    <br>
    <label>Enter Any Type Of Living Thing</label>
    <input name="livThing">
    <br>
    <label>Say Something Nice To Someone</label>
    <input name="nice">
    <br>
    <h3>Send And Show a Friend</h3>
    <button>Send</button>
    </form>
</body>
</html>
