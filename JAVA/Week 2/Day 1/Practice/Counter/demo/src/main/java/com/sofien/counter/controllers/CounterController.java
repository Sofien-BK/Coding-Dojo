package com.sofien.counter.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import jakarta.servlet.http.HttpSession;

@Controller
@RequestMapping("/")
public class CounterController {
	
	@GetMapping("")
	public String welcomePage(HttpSession session) {
		
	    Integer counter = (Integer) session.getAttribute("counter");

	    if (counter == null) {
	        counter = 0;
	    }

	    counter++;

	    session.setAttribute("counter", counter);

	    session.setAttribute("count", counter);
		return "welcome.jsp"; 
	}
	
	@GetMapping("/counter")
	public String counterPage(Model model, HttpSession ss) {
		 Integer x = (Integer) ss.getAttribute("count"); 
		    
		    if (x == null) {
		        x = 0;
		    }

		    model.addAttribute("count", x);
		return "count.jsp"; 
	}
}
