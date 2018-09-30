//
//  GameScene.swift
//  Soccer
//
//  Created by Tao Ong on 4/8/18.
//  Copyright © 2018 Tao Ong. All rights reserved.
//

import SpriteKit
import GameplayKit

class GameScene: SKScene {

    var leftButton = SKSpriteNode()
    var rightButton = SKSpriteNode()
    var leftTouches : [UITouch] = []
    var rightTouches : [UITouch] = []
    var player = SKSpriteNode()
    var test = 0
    
    
    override func sceneDidLoad() {

        leftButton = self.childNode(withName: "left") as! SKSpriteNode
        rightButton = self.childNode(withName: "right") as! SKSpriteNode
        player = self.childNode(withName: "player") as! SKSpriteNode
    }
    
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        for touch in touches {
            let location = touch.location(in: self)
            if leftButton.contains(location) {
                leftTouches.append(touch)
            }
            if rightButton.contains(location) {
                rightTouches.append(touch)
            }
        }
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        for touch in touches {
            let location = touch.location(in: self)
            for t in leftTouches {
                if touch == t {
                    if leftButton.contains(location) == false {
                        
                    }
                }
            }
        }
    }
   
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        for touch in touches {
            for t in leftTouches {
                if touch == t {
                    leftTouches.
                }
            }
        }
    }
    
    override func update(_ currentTime: TimeInterval) {
        if leftButtonDown == true {
            player.run(SKAction.rotate(byAngle: 0.04, duration: 0))
        }
        if rightButtonDown == true {
            player.run(SKAction.rotate(byAngle: -0.04, duration: 0))
        }
    }
}
