#include "fluidsynth.h"
int main()
{
    fluid_settings_t *settings;
    fluid_synth_t *synth;
    fluid_player_t *player;
    fluid_audio_driver_t *adriver;
    settings = new_fluid_settings();
    synth = new_fluid_synth(settings);
    adriver = new_fluid_audio_driver(settings, synth);
    /* process command line arguments */
    fluid_synth_sfload(synth, "fluidsynth\\GeneralUser_GS.sf2", 1);
    while (1)
    {
        char c = getchar();
        if (c == 'a')
        {
            player = new_fluid_player(synth);
            fluid_player_add(player, "fluidsynth\\tmp.mid");
            /* play the midi files, if any */
            fluid_player_play(player);
            /* wait for playback termination */
            fluid_player_join(player);
            delete_fluid_player(player);
        }
        else
            return 0;
    }
    /* cleanup */
    delete_fluid_audio_driver(adriver);
    delete_fluid_synth(synth);
    delete_fluid_settings(settings);
    return 0;
}