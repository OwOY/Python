import random
import queue

class RPGGame:
    def charactor_info(self, name):
        charactor = {
            'gobling' : {
                'health':40,
                'attack':15,
                'shield':0
            },
            'flareon'  : {
                'health':80,
                'attack':15,
                'shield':35
            },
            'devil_shepherd_dog' : {
                'health':50,
                'attack':20,
                'shield':15
            },
            'monster' : {
                'health':200,
                'attack':30
            }
        }
        return charactor[name]
    
    def choose_charctor(self, number):
        charactor_dict = {
            1:'gobling',
            2:'flareon',
            3:'devil_shepherd_dog'
        }
        return charactor_dict[number]
    
    def trans_chinese_name(self, eng_name):
        charactor_dict = {
            'gobling':'哥布林',
            'flareon':'火精靈',
            'devil_shepherd_dog':'惡狼犬'
        }
        return charactor_dict[eng_name]
    
    def attack_monster(self, monster_info, charactor_info):
        monster_alive = True
        monster_info['health'] = monster_info['health'] - charactor_info['attack']
        if monster_info['health'] < 0:
            monster_alive = False
        return monster_alive
    
    def attack_charactor(self, monster_info, charactor_info):
        charactor_alive = True
        if charactor_info['shield']:
            charactor_info['shield'] = charactor_info['shield'] - monster_info['attack']
            if charactor_info['shield'] < 0:
                charactor_info['health'] = charactor_info['health'] + charactor_info['shield']
                charactor_info['shield'] = 0
        else:
            charactor_info['health'] = charactor_info['health'] - monster_info['attack']
        if charactor_info['health'] < 0:
            charactor_alive = False
        return charactor_alive
    
    def battle(self, charactor, monster_info, charactor_info):
        print('===========戰鬥開始===========')
        while True:
            monster_alive = self.attack_monster(monster_info, charactor_info)
            print(f'對敵方進行攻擊，敵方所剩血量{monster_info["health"]}')
            if not monster_alive:
                print('戰鬥勝利！')
                break
            
            charactor_alive = self.attack_charactor(monster_info, charactor_info)
            print(f'敵方襲擊猛烈，{self.trans_chinese_name(charactor)}，所剩血量{charactor_info["health"]}，護盾{charactor_info["shield"]}')
            if not charactor_alive:
                print(f'{self.trans_chinese_name(charactor)}戰死')
                break
        print('===========戰鬥結束===========\n')
            
    def main(self):
        # charactor_choose = int(input('請選擇要出場的角色。 1.哥布林 2.火精靈 3.惡狼犬'))
        q = queue.Queue()
        for i in random.sample(range(1, 4), 3):
            q.put(i)
        monster_info = self.charactor_info('monster')
        print(f"你遇到了魔獸\n魔獸的狀態：血量：{monster_info['health']}攻擊力：{monster_info['attack']}\n")
        
        while monster_info['health'] > 0:
            charactor_choose = q.get()
            charactor = self.choose_charctor(charactor_choose)
            print(f'出來吧！就決定是你了！{self.trans_chinese_name(charactor)}')
            charactor_info = self.charactor_info(charactor)
            print(f'{self.trans_chinese_name(charactor)}狀態：血量：{charactor_info["health"]}，攻擊：{charactor_info["attack"]}，護盾：{charactor_info["shield"]}\n')
            self.battle(charactor, monster_info, charactor_info)
            if q.empty():
                print('角色全死亡，戰鬥失敗')
                break
            
if __name__ == '__main__':
    RPGGame().main()