//
//  Person.swift
//  FirstProject
//
//  Created by Tao Ong on 11/12/17.
//  Copyright © 2017 Tao Ong. All rights reserved.
//

import Foundation

class Person {
    
    var name : String
    var height : Int
    var hobbies : [String]
    
    init(name : String, hobbies : [String]) {
        self.name = name
        self.height = 12
        self.hobbies = hobbies
    }
    
    func grow() -> Void {
        height += 1
    }
    
    func addHobby(newHobby : String) -> Void {
        hobbies.append(newHobby)
    }
}
