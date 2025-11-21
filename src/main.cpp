#define SDL_MAIN_USE_CALLBACKS
#include <SDL3/SDL_main.h>
#include <Engine/Precompiled.h>

static struct runtime_t {
    int x, y;
} rt;

SDL_AppResult SDL_AppInit(void** appstate, int argc, char** argv) {
    *appstate = static_cast<void*>(&rt);
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppIterate(void* appstate) {
    return SDL_APP_CONTINUE;
}

SDL_AppResult SDL_AppEvent(void* appstate, SDL_Event* event) {
    switch (event->type) {
    case SDL_EVENT_QUIT:
        return SDL_APP_SUCCESS;
    default:
        return SDL_APP_CONTINUE;
    }
}

void SDL_AppQuit(void* appstate, SDL_AppResult result) {
}