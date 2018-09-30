//
//  GameScene.swift
//  Car
//
//  Created by Tao Ong on 4/15/18.
//  Copyright © 2018 Tao Ong. All rights reserved.
//

import SpriteKit
import GameplayKit
import CoreMotion

class GameScene: SKScene, SKPhysicsContactDelegate {
    
    var car = SKSpriteNode()
    var left = SKSpriteNode()
    var right = SKSpriteNode()
    var leftFingers = 0
    var rightFingers = 0
    
    override func sceneDidLoad() {
        car = self.childNode(withName: "car") as! SKSpriteNode
        left = self.childNode(withName: "left") as! SKSpriteNode
        right = self.childNode(withName: "right") as! SKSpriteNode
        let motionManager = CMMotionManager()
        motionManager.startAccelerometerUpdates()
        self.physicsWorld.contactDelegate = self

    }
    
    func didBegin(_ contact: SKPhysicsContact) {
        <#code#>
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        for t in touches {
            if left.contains(t.location(in: self)) {
                leftFingers += 1
            }
            if right.contains(t.location(in: self)) {
                rightFingers += 1
            }
        }
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        for t in touches {
            if left.contains(t.location(in: self)) {
                leftFingers -= 1
            }
            if right.contains(t.location(in: self)) {
                rightFingers -= 1
            }
        }
    }
    
    override func update(_ currentTime: TimeInterval) {
        
        if leftFingers > 0 {
            car.run(SKAction.rotate(byAngle: 0.1, duration: 0))
        }
        if rightFingers > 0 {
            car.run(SKAction.rotate(byAngle: -0.1, duration: 0))
        }
        if leftFingers > 0 && rightFingers > 0 {
            
        }
        
        if let scoreInt = Int(score.text!), let bestScoreInt = Int(bestScore.text!) {
            
        }
    }
    
    
}
