<page>
    <actionBar title="Home" />
    <gridLayout>
        <label class="info">
            <formattedString>
                <span class="fas" text="&#xf135;" />
                <span text=" {message}" />
            </formattedString>
        </label>
        <!-- This is the whole page -->
        <drawer bind:this={drawer} class="drawer">
            <gridlayout prop:leftDrawer width="300" backgroundColor="white" rows="auto, *">
                <stacklayout row="0">
                    <stacklayout backgroundColor="#eeeeee" padding="25">
                        <gridlayout columns="80, *" height="100">
                            <stacklayout col="0" class="avatar">
                                <label text="JS" />
                            </stacklayout>
                        </gridlayout>
                        <stacklayout>
                            <label text="John Smith" fontWeight="bold" />
                            <label text="john.smith@example.com" />
                        </stacklayout>
                    </stacklayout>
                    <stacklayout>
                        {#if quests}
                            {#if $quests.loading}
                                <label>Loading...</label>
                            {:else if $quests.error}
                                <label>Error {$quests.error.message}</label>
                            {:else}
                                {#each $quests.data.quests as quest}
                                    <button text="&#xf02d; {quest.title}" class="fas button" on:tap={() => onQuestSelected(quest.id)} />
                                {/each}
                            {/if}
                        {/if}
                    </stacklayout>
                    <flexboxlayout>
                        <button text="&#xf013;" class="fas btn-ico" />
                        <button text="&#xf0ca;" class="fas btn-ico" />
                        <button text="&#xf802;" class="fas btn-ico" />
                    </flexboxlayout>
                </stacklayout>
            </gridlayout>
    
            <stacklayout prop:mainContent backgroundColor="white">
                <button on:tap={onOpenDrawer} text="Open Drawer" width="250" marginTop="25" />
                <!-- <button on:tap={getQuests} data-cy="query">Get Quests</button> -->
                {#if quest}
                    {#if $quest.loading}
                        <label>Loading...</label>
                    {:else if $quest.error}
                        <label>Error {$quests.error.message}</label>
                    {:else}
                        {#each $quest.data.quests as q} <!-- should only be one -->
                            <label>{q.title}</label>
                            <!-- <lable>{q.something}</lable> -->
                            <!-- {#if q.parentId} -->
                            <label>{q.description}</label>
                            <!-- {#each Object.entries(q) as [key, value]}
                                <label>{key}: {value}</label>
                            {/each} -->
                        {/each}
                    {/if}
                {/if}
            </stacklayout>
        </drawer>
    </gridLayout>
</page>

<script lang="ts">
    // let quests = ["something", "something else"]
    let message: string = "Blank Svelte Native App"
    let quests: any;
    import { Drawer } from '@nativescript-community/ui-drawer';
    let drawer: Drawer;
    let quest: any;

    function onOpenDrawer() {
        // getQuests()
        getRoot()
        drawer.open()
    }

    function onQuestSelected(id: string) {
        getQuest(id)
        drawer.close()
    }

    function onCloseDrawer() {
        drawer.close()
    }

    import { InMemoryCache } from '@apollo/client/core';

    // function createApolloClient(authToken: string) {
    //     const link = new HttpLink({
    //         uri: "http://10.0.2.2:6060/graphql",
    //         headers: {
    //         Authorization: `Bearer ${authToken}`,
    //         },
    //     });
    //     const client = new ApolloClient({
    //         link,
    //         cache,
    //     });
    //     return client;
    // }
    import { gql } from '@apollo/client/core';
    // import { setClient } from "svelte-apollo";

    const GET_QUESTS = gql`
    query {
        quests {
            id,
            title,
            parentId
        }
    }`

    const GET_ROOT = gql`
    query {
        quests(type:"journal") {
            id,
            title
        }
    }`

    const GET_QUEST_DETAILS = gql`
    query quests($id: Int!) {
        quests(id: $id) {
            id,
            type,
            title,
            description,
            parentId,
            share,
            secret
        }
    }`

    import { SvelteApolloClient } from "svelte-apollo-client";
    
    export const client = SvelteApolloClient({
        uri: "http://10.0.2.2:6060/graphql",
        cache: new InMemoryCache(),
    });
    export let authToken: string;

    import { onMount } from "svelte";
    import { Http } from '@nativescript/core'

    function getQuests () {
        quests = client.query(GET_QUESTS);
        $: quests && console.log($quests)
    }

    function getRoot() {
        quests = client.query(GET_ROOT)
        $: quests && console.log($quests)
    }

    function getQuest(id: any) {
        quest = client.query(GET_QUEST_DETAILS, {
            variables: { id }
        })
        $: quest && console.log($quest)
    }

    onMount(async () => {
        
        Http.getJSON('http://10.0.2.2:6060/Greetings').then(
            (result: any) => {
                console.log(result)
            },
            e => {
                console.log(e)
            }
        );
    });

</script>

<style>
    /* 
    File name: fa-regular-400.ttf 
    Font name: Font Awesome 5 Free
    */
    .fas {
        font-family: "Font Awesome 5 Free", "fa-solid-900";
        font-weight: 900;
    }

    Button {
        background-color: #b52e31;
        color: white;
    }

    .info .fas {
        color: #3A53FF;
    }

    .info {
        font-size: 20;
        /* horizontal-align: center; */
        vertical-align: center;
    }

    ActionBar {
        background-color: #b52e31;
        color: white;
    }
    .avatar {
        background-color: #b52e31;
        border-radius: 40;
        height: 80;
        vertical-align: middle;
    }
    .avatar Label {
        vertical-align: middle;
        font-size: 30;
        color: white;
    }
    .drawer .button {
        background-color: transparent;
        margin: 0;
        padding: 0;
        border-color: #ccc;
        z-index: 0;
        border-width: 0 0 0.5 0;
        color: #222222;
        text-align: left;
        padding-left: 25;
        height: 50;
        font-size: 14;
    }
    .drawer .button:highlighted {
        background-color: #eeeeee;
        color: #222222;
    }

    .btn-ico {
        width:50em;
    }
    
</style>
