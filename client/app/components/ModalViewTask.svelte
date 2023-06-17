<!-- a task cannot have children, so viewing it is a popup with details -->
<frame id="detail-page-frame">
  <page height="50%">
    <actionBar title="Create Quest" />
    <docklayout stretchLastChild="true">
        <stacklayout dock="bottom" orientation="horizontal">
            <button text="Cancel" on:tap="{onCloseModal}" />
            <button text="Save" on:tap="{onCloseModal}" />
        </stacklayout>

        <stacklayout dock="top">
            <textfield hint="Title" />
        </stacklayout>
    </docklayout>
  </page>
</frame>

<script>
    import { closeModal } from 'svelte-native'
    export let task;
    console.log(task.id)
    console.log(task.description)

    function onCloseModal() {
        task = { title: "test" }
        closeModal(task)
    }
</script>