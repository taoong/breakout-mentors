//
//  GameScene.swift
//  PixelPainter
//
//  Created by Tao Ong on 3/19/18.
//  Copyright © 2018 Tao Ong. All rights reserved.
//

import SpriteKit
import GameplayKit

class GameScene: SKScene {
    
    var main = SKSpriteNode()
    var red = SKSpriteNode()
    var orange = SKSpriteNode()
    var yellow = SKSpriteNode()
    var green = SKSpriteNode()
    var blue = SKSpriteNode()
    var menuOpen = false
    
    override func sceneDidLoad() {
        main = self.childNode(withName: "main") as! SKSpriteNode
        red = self.childNode(withName: "red") as! SKSpriteNode
        orange = self.childNode(withName: "orange") as! SKSpriteNode
        yellow = self.childNode(withName: "yellow") as! SKSpriteNode
        green = self.childNode(withName: "green") as! SKSpriteNode
        blue = self.childNode(withName: "blue") as! SKSpriteNode
        closeColorMenu()
    }
    
    func openColorMenu() {
        red.isHidden = false
        orange.isHidden = false
        yellow.isHidden = false
        green.isHidden = false
        blue.isHidden = false
        menuOpen = true
    }
    
    func closeColorMenu() {
        red.isHidden = true
        orange.isHidden = true
        yellow.isHidden = true
        green.isHidden = true
        blue.isHidden = true
        menuOpen = false
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        let location = touches.first?.location(in: self)
        if menuOpen == true {
            if main.contains(location!) {
                closeColorMenu()
            }
            else if red.contains(location!) {
                main.color = UIColor.red
            }
            else if orange.contains(location!) {
                main.color = UIColor.orange
            }
            else if yellow.contains(location!) {
                main.color = UIColor.yellow
            }
            else if green.contains(location!) {
                main.color = UIColor.green
            }
            else if blue.contains(location!) {
                main.color = UIColor.blue
            }
        } else {
            if main.contains(location!) {
                openColorMenu()
            }
        }
    }
    
    override func update(_ currentTime: TimeInterval) {
        
    }
}
