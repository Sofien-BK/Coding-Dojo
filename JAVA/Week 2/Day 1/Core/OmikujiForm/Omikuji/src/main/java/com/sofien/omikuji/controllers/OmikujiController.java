package com.sofien.omikuji.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import jakarta.servlet.http.HttpSession;

@Controller
@RequestMapping("/omikuji")
public class OmikujiController {
	
	@GetMapping("")
	public String omikujiForm(){
		return "form.jsp"; 
	}
	
	@PostMapping("/processOmikuji")
	public String form(@RequestParam("number") int number ,
			@RequestParam("city") String city ,
			@RequestParam("person") String person ,
			@RequestParam("hobby") String hobby,
			@RequestParam("livThing") String livThing,
			@RequestParam("nice") String nice,
			HttpSession s) {
		
		s.setAttribute("num", number);
		s.setAttribute("city", city);
		s.setAttribute("per", person);
		s.setAttribute("hobby", hobby);
		s.setAttribute("liv", livThing);
		s.setAttribute("nice", nice);
		
		return "redirect:/omikuji/result";
	}
	
	@GetMapping("/result")
	public String result(){
		
		return "omikuji.jsp"; 
	}
}
