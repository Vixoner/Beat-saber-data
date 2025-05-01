def process(data):
    new_data = []
    important_data = ['rank','totalPlayCount','topPp','averageAccuracy','watchedReplays','replaysWatched','countryRank','top1Count','totalImprovementsCount',
                      'averageRank','maxStreak','sspPlays','ssPlays','spPlays','sPlays','aPlays']

    for entry in data:
        player_list = entry["data"]
        for player in player_list:
            if 'scoreStats' in player:
                for key, value in player['scoreStats'].items():
                    player[key] = value
                del player['scoreStats']

            player['replaysWatched'] = player['authorizedReplayWatched'] + player['anonimusReplayWatched']

            new_player = {}

            if player['topPp'] > 0 and player['aPlays'] >= 0 and player['top1Count'] >= 0:
                for key, value in player.items():
                    if key in important_data:
                        new_player[key] = value

                new_data.append(new_player)

    return new_data
