package com.dakichi.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/daikichi")
public class DaikichiController {
	
	@GetMapping("")
	public String welcome() {
		return "Welcome!";
	}
	@GetMapping("/today")
	public String luck() {
		return "Today you will find luck in all your endeavors!";
	}
	@GetMapping("/tomorrow")
	public String arise() {
		return "Tomorrow, an opportunity will arise, so be sure to be open to new ideas!";
	}
	
}
