package com.hoppers.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class HoppersController {
	
	@GetMapping("")
	public String index(Model model) {
		String name = "Copper Wire";
        String itemName = "Copper wire";
        double price = 5.25;
        String description = "Metal strips, also an illustration of nanoseconds.";
        String vendor = "Little Things Corner Store";
        
        model.addAttribute("name" , name); 
        model.addAttribute("itemName" , itemName);
        model.addAttribute("price" , price);
        model.addAttribute("description" , description);
        model.addAttribute("vendor" , vendor);
        
        return "index.jsp";
	}
}
