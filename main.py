from spaceInvadersGUI import *

score = 0
go_to_the_game = False
while True:
    if not go_to_the_game:
        show_opening_screen()
        go_to_the_game = True

    clock.tick(FPS)
    win.fill(BLACK)
    win.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #The software will check if the key that was "pressed" is the space bar 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #The software will callthe shoot function from the Player class
                my_player.shoot()

    all_sprites.draw(win)
    all_sprites.update()
    user_score.draw(win)

    #A variable that will contain the list of collisions returned by the groupcollide function between the sprites of the groups
    bullet_and_meteor_collide = pygame.sprite.groupcollide(meteors, my_player.bullets, True, True)
    #A for loop that will go through each element in the list bullets_and_meteor_collide_ and recreate the meteor that the function groupcollide deletes, increase the user's score by 1 and will create a large explosion upon collision
    for collision in bullet_and_meteor_collide:
        score += 1
        user_score.set_text(str(score))
        create_meteor()
        create_explosion(collision.rect.center, 'large')

    #A variable that will contain the list of collisions returned by the spritecollide function between the sprites
    player_and_meteor_collide = pygame.sprite.spritecollide(my_player, meteors, True)
    #A for loop that will go through each element in the list player_and_meteor_collide_ and recreate the meteor that the function spritecollide deletes, decrease the user's score by 1 and will create a small explosion upon collision
    for collision in player_and_meteor_collide:
        score -= 2
        user_score.set_text(str(score))
        create_meteor()
        create_explosion(collision.rect.center, 'small')

    #gets_hit = pygame.spritecollideany(my_player, meteors)
    #if gets_hit:
    #    my_player.change_color()

    pygame.display.update()
