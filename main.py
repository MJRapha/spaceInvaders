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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.shoot()

    all_sprites.draw(win)
    all_sprites.update()
    user_score.draw(win)

    bullet_and_meteor_collide = pygame.sprite.groupcollide(meteors, my_player.bullets, True, True)
    for collision in bullet_and_meteor_collide:
        score += 1
        user_score.set_text(str(score))
        create_meteor()
        create_explosion(collision.rect.center, 'large')

    player_and_meteor_collide = pygame.sprite.spritecollide(my_player, meteors, True)
    for collision in player_and_meteor_collide:
        score -= 2
        user_score.set_text(str(score))
        create_meteor()
        create_explosion(collision.rect.center, 'small')

    #gets_hit = pygame.spritecollideany(my_player, meteors)
    #if gets_hit:
    #    my_player.change_color()

    pygame.display.update()
