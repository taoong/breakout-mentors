//
//  ViewController.swift
//  MyFirstApp
//
//  Created by Tao Ong on 2/25/18.
//  Copyright © 2018 Tao Ong. All rights reserved.
//

import UIKit

var model = Model()

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBOutlet weak var label1: UILabel!
    
    @IBAction func button1(_ sender: Any) {
        label1.text = model.name
    }
    
}

