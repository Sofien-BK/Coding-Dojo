package com.daikichipath.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/daikichi")
public class DaikichiRoutes {
	
	@GetMapping("/travel/{city}")
	public String traveling (@PathVariable("city") String city) {
		return String.format("Congratulations! You will soon travel to %s",city);
		}
	
	@GetMapping("/lotto/{num}")
	public String lottoing (@PathVariable("num") int num) {
		if (num % 2==1 ) {
			return "You have enjoyed the fruits of your labor but now is a great time to spend time with family and friends.";
		}else {
			return "You will take a grand journey in the near future, but be weary of tempting offers";
		}
		}
}
