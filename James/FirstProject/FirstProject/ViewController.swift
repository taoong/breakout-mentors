//
//  ViewController.swift
//  FirstProject
//
//  Created by Tao Ong on 11/12/17.
//  Copyright © 2017 Tao Ong. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    var person = Person(name: "Tao", hobbies : ["Soccer"])
    
    @IBOutlet weak var name: UILabel!
    @IBOutlet weak var height: UILabel!
    @IBOutlet weak var hobbies: UILabel!
    
    @IBAction func grow(_ sender: Any) {
        person.grow()
        updateScreen()
    }
    
    func updateScreen() -> Void {
        name.text = person.name
        height.text = String(person.height)
        hobbies.text = String(describing: person.hobbies)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        updateScreen()
        
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    

}

